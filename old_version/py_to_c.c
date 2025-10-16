#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

#define LINE_BUF 1024
#define INITIAL_VARS 64
#define MAX_TRIES 5

typedef enum { VT_INT, VT_STR } VarType;

typedef struct {
    char *name;
    VarType type;
    long long int_val;
    char *str_val;
} Variable;

typedef struct {
    Variable *arr;
    size_t len;
    size_t cap;
} VarStore;

void vs_init(VarStore *vs) {
    vs->cap = INITIAL_VARS;
    vs->len = 0;
    vs->arr = calloc(vs->cap, sizeof(Variable));
    if (!vs->arr) { perror("calloc"); exit(1); }
}
void vs_free(VarStore *vs) {
    for (size_t i=0;i<vs->len;i++) {
        free(vs->arr[i].name);
        if (vs->arr[i].type == VT_STR) free(vs->arr[i].str_val);
    }
    free(vs->arr);
}
Variable *vs_find(VarStore *vs, const char *name) {
    for (size_t i=0;i<vs->len;i++) if (strcmp(vs->arr[i].name, name)==0) return &vs->arr[i];
    return NULL;
}
int vs_index(VarStore *vs, const char *name) {
    for (size_t i=0;i<vs->len;i++) if (strcmp(vs->arr[i].name, name)==0) return (int)i;
    return -1;
}
void vs_ensure_cap(VarStore *vs) {
    if (vs->len < vs->cap) return;
    vs->cap *= 2;
    vs->arr = realloc(vs->arr, vs->cap * sizeof(Variable));
    if (!vs->arr) { perror("realloc"); exit(1); }
}
void vs_set_int(VarStore *vs, const char *name, long long val) {
    Variable *v = vs_find(vs, name);
    if (v) {
        if (v->type == VT_STR) { free(v->str_val); v->str_val = NULL; }
        v->type = VT_INT;
        v->int_val = val;
        return;
    }
    vs_ensure_cap(vs);
    Variable *nv = &vs->arr[vs->len++];
    nv->name = strdup(name);
    nv->type = VT_INT;
    nv->int_val = val;
    nv->str_val = NULL;
}
void vs_set_str(VarStore *vs, const char *name, const char *s) {
    Variable *v = vs_find(vs, name);
    if (v) {
        if (v->type == VT_STR) { free(v->str_val); }
        v->type = VT_STR;
        v->str_val = strdup(s);
        return;
    }
    vs_ensure_cap(vs);
    Variable *nv = &vs->arr[vs->len++];
    nv->name = strdup(name);
    nv->type = VT_STR;
    nv->str_val = strdup(s);
}
int vs_delete(VarStore *vs, const char *name) {
    int idx = vs_index(vs, name);
    if (idx < 0) return 0;
    free(vs->arr[idx].name);
    if (vs->arr[idx].type == VT_STR) free(vs->arr[idx].str_val);
    // shift left
    for (size_t i = idx; i+1 < vs->len; ++i) vs->arr[i] = vs->arr[i+1];
    vs->len--;
    return 1;
}
void vs_clear(VarStore *vs) {
    for (size_t i=0;i<vs->len;i++) {
        free(vs->arr[i].name);
        if (vs->arr[i].type == VT_STR) free(vs->arr[i].str_val);
    }
    vs->len = 0;
}

void sleep_seconds(int s) {
#ifdef _WIN32
    Sleep(s * 1000);
#else
    sleep(s);
#endif
}

void trim_newline(char *s) {
    size_t n = strlen(s);
    while (n>0 && (s[n-1]=='\n' || s[n-1]=='\r')) { s[n-1]='\0'; n--; }
}

void clear_screen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void print_variables(VarStore *vs) {
    if (vs->len==0) {
        printf("<NameError>:Variable '%s' is empty\n", "{}");
        return;
    }
    puts("Variables :");
    for (size_t i=0;i<vs->len;i++) {
        Variable *v = &vs->arr[i];
        if (v->type == VT_INT)
            printf("%s = %lld\n", v->name, v->int_val);
        else
            printf("%s = %s\n", v->name, v->str_val);
    }
}

int is_integer_str(const char *s) {
    if (!s || *s=='\0') return 0;
    const char *p = s;
    if (*p=='+' || *p=='-') p++;
    if (!*p) return 0;
    while (*p) {
        if (!isdigit((unsigned char)*p)) return 0;
        p++;
    }
    return 1;
}

// split tokens like Python .split() by whitespace.
// returns an array of char* (must be freed). tokens_out set to count.
char **split_tokens(const char *line, int *tokens_out) {
    char *buf = strdup(line);
    char *p = buf;
    char *token;
    char **arr = NULL;
    int cap = 0, len = 0;
    while ((token = strsep(&p, " \t")) != NULL) {
        if (*token == '\0') continue;
        if (len+1 > cap) {
            cap = cap ? cap*2 : 8;
            arr = realloc(arr, cap * sizeof(char*));
        }
        arr[len++] = strdup(token);
    }
    free(buf);
    *tokens_out = len;
    return arr;
}
void free_tokens(char **toks, int n) {
    for (int i=0;i<n;i++) free(toks[i]);
    free(toks);
}

// forward
void process_tokens(char **tokens, int ntoks, VarStore *vs, char **username_ref);

void reader_run(const char *filename, VarStore *vs, char **username_ref) {
    printf("======================================================\n");
    printf("Opening File...\n");
    printf("======================================================\n");
    FILE *f = fopen(filename, "r");
    if (!f) {
        printf("<FileNotFound> : The file %s couldn't be imported\n", filename);
        return;
    }
    char line[LINE_BUF];
    while (fgets(line, sizeof(line), f)) {
        trim_newline(line);
        int n;
        char **tokens = split_tokens(line, &n);
        process_tokens(tokens, n, vs, username_ref);
        free_tokens(tokens, n);
    }
    fclose(f);
}

void handle_int_cmd(char **tokens, int ntoks, VarStore *vs) {
    // expect: int var = value
    if (ntoks < 4 || strcmp(tokens[2], "=") != 0) {
        puts("<SyntaxError>:Invalid int command");
        return;
    }
    const char *var = tokens[1];
    const char *raw = tokens[3];
    if (!is_integer_str(raw)) {
        puts("<ValueError>:Not An Integer");
        return;
    }
    long long val = atoll(raw);
    vs_set_int(vs, var, val);
}

void handle_str_cmd(char **tokens, int ntoks, VarStore *vs) {
    // expect: str var = some_token (only token 3 used like python)
    if (ntoks < 4 || strcmp(tokens[2], "=") != 0) {
        puts("<SyntaxError>:Invalid str command");
        return;
    }
    const char *var = tokens[1];
    const char *raw = tokens[3];
    vs_set_str(vs, var, raw);
}

void handle_print_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 2) { puts("<SyntaxError>:Invalid print command"); return; }
    const char *var = tokens[1];
    Variable *v = vs_find(vs, var);
    if (!v) { printf("<NameError>:Variable %s not Defined\n", var); return; }
    if (v->type == VT_INT) printf("%lld\n", v->int_val);
    else printf("%s\n", v->str_val);
}

void handle_type_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 2) { puts("<SyntaxError>:Invalid type command"); return; }
    const char *var = tokens[1];
    Variable *v = vs_find(vs, var);
    if (!v) { puts("<NameError:Variable not defined"); return; }
    if (v->type == VT_INT) puts("<class 'int'>");
    else puts("<class 'str'>");
}

void handle_add_cmd(char **tokens, int ntoks, VarStore *vs) {
    // add a + b  (len == 4)
    if (ntoks != 4) { puts("<SyntaxError>:Invalid add command"); return; }
    const char *a = tokens[1];
    const char *b = tokens[3];
    Variable *va = vs_find(vs, a);
    Variable *vb = vs_find(vs, b);
    if (!va || !vb) { printf("<NameError>:Variable '%s' or/and '%s' not Defined\n", a, b); return; }
    if (va->type != VT_INT || vb->type != VT_INT) { puts("<TypeError>: Not an integer"); return; }
    printf("%lld\n", va->int_val + vb->int_val);
}

void handle_sub_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 4) { puts("<SyntaxError>:Invalid sub command"); return; }
    const char *a = tokens[1];
    const char *b = tokens[3];
    Variable *va = vs_find(vs, a);
    Variable *vb = vs_find(vs, b);
    if (!va || !vb) { printf("<NameError>:Variable '%s' or/and '%s' not Defined\n", a, b); return; }
    if (va->type != VT_INT || vb->type != VT_INT) { puts("<TypeError>: Not an integer"); return; }
    printf("%lld\n", va->int_val - vb->int_val);
}

void handle_mul_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 4) { puts("<SyntaxError>:Invalid mul command"); return; }
    const char *a = tokens[1];
    const char *b = tokens[3];
    Variable *va = vs_find(vs, a);
    Variable *vb = vs_find(vs, b);
    if (!va || !vb) { printf("<NameError>:Variable '%s' or/and '%s' not Defined\n", a, b); return; }
    if (va->type != VT_INT || vb->type != VT_INT) { puts("<TypeError>: Not an integer"); return; }
    printf("%lld\n", va->int_val * vb->int_val);
}

void handle_div_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 4) { puts("<SyntaxError>:Invalid div command"); return; }
    const char *a = tokens[1];
    const char *b = tokens[3];
    Variable *va = vs_find(vs, a);
    Variable *vb = vs_find(vs, b);
    if (!va || !vb) { printf("<NameError>:Variable '%s' or/and '%s' not Defined\n", a, b); return; }
    if (va->type != VT_INT || vb->type != VT_INT) { puts("<TypeError>: Not an integer"); return; }
    if (vb->int_val == 0) { puts("<ZeroDivisionError>: Can't Divide by zero"); return; }
    double res = (double)va->int_val / (double)vb->int_val;
    printf("%g\n", res);
}

void handle_mod_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 2) { puts("<SyntaxError>:Invalid mod command"); return; }
    const char *a = tokens[1];
    Variable *va = vs_find(vs, a);
    if (!va) { printf("<NameError>:Variable '%s' not Defined\n", a); return; }
    if (va->type != VT_INT) { puts("<ValueError> : not an integer"); return; }
    long long v = va->int_val;
    if (v < 0) v = -v;
    printf("%lld\n", v);
}

void handle_rename_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 3) { puts("<SyntaxError>:Invalid rename command"); return; }
    const char *oldn = tokens[1];
    const char *newn = tokens[2];
    Variable *vold = vs_find(vs, oldn);
    Variable *vnew = vs_find(vs, newn);
    if (!vold) { printf("<NameError>:Variable '%s' not Defined\n", oldn); return; }
    if (vnew) { printf("<NameError>:Variable '%s' already exists\n", newn); return; }
    // copy old to new
    if (vold->type == VT_INT) vs_set_int(vs, newn, vold->int_val);
    else vs_set_str(vs, newn, vold->str_val);
    vs_delete(vs, oldn);
    printf("Renamed %s to %s\n", oldn, newn);
}

void handle_purge_cmd(VarStore *vs) {
    if (vs->len) vs_clear(vs);
    else printf("<NameError>:List '%s' is empty\n", "{}");
}

void handle_del_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 2) { puts("<SyntaxError>:Invalid del command"); return; }
    const char *a = tokens[1];
    if (!vs_delete(vs, a)) printf("<NameError> : Variable %s not Defined\n", a);
}

void handle_list_cmd(VarStore *vs) {
    print_variables(vs);
}

void handle_loop_cmd(char **tokens, int ntoks, VarStore *vs) {
    if (ntoks != 3) { puts("<SyntaxError>:Invalid loop command"); return; }
    if (!is_integer_str(tokens[1])) { puts("<SyntaxError>:Invalid repeat count"); return; }
    int times = atoi(tokens[1]);
    const char *var = tokens[2];
    Variable *v = vs_find(vs, var);
    if (!v) { printf("<NameError>:Variable '%s' not Defined\n", var); return; }
    for (int i=0;i<times;i++) {
        if (v->type == VT_INT) printf("%lld\n", v->int_val);
        else printf("%s\n", v->str_val);
    }
}

void handle_reset_username_cmd(char **tokens, int ntoks, char **username_ref) {
    if (ntoks != 3) { puts("<SyntaxError>:Invalid reset username command"); return; }
    const char *newname = tokens[2];
    free(*username_ref);
    *username_ref = strdup(newname);
    FILE *f = fopen("authentication.fermlog", "w");
    if (f) {
        fprintf(f, "Username : %s\n", *username_ref);
        fclose(f);
    }
    printf("Changed Username To %s\n", *username_ref);
}

void handle_ferm_run_cmd(char **tokens, int ntoks, VarStore *vs, char **username_ref) {
    if (ntoks != 3) { puts("<SyntaxError>:Invalid ferm run command"); return; }
    const char *fname = tokens[2];
    reader_run(fname, vs, username_ref);
}

void process_tokens(char **tokens, int ntoks, VarStore *vs, char **username_ref) {
    if (ntoks == 0) return;
    const char *cmd = tokens[0];

    // allowed commands list (mirrors python list_command)
    const char *allowed[] = {"int","print","add","sub","mod","type","rename","list","purge","mul","div","ferm","del","find","loop","str","exit","reset"};
    int ok = 0;
    for (size_t i=0;i<sizeof(allowed)/sizeof(allowed[0]);i++) if (strcmp(cmd, allowed[i])==0) { ok = 1; break; }
    if (!ok) { puts("<SyntaxError>:Invalid Command"); return; }

    if (strcmp(cmd, "int")==0) handle_int_cmd(tokens, ntoks, vs);
    else if (ntoks==3 && strcmp(cmd, "reset")==0 && strcmp(tokens[1], "username")==0) handle_reset_username_cmd(tokens, ntoks, username_ref);
    else if (strcmp(cmd, "type")==0) handle_type_cmd(tokens, ntoks, vs);
    else if (ntoks==2 && strcmp(cmd, "print")==0) handle_print_cmd(tokens, ntoks, vs);
    else if (ntoks==4 && strcmp(cmd, "add")==0) handle_add_cmd(tokens, ntoks, vs);
    else if (ntoks==4 && strcmp(cmd, "sub")==0) handle_sub_cmd(tokens, ntoks, vs);
    else if (ntoks==4 && strcmp(cmd, "mul")==0) handle_mul_cmd(tokens, ntoks, vs);
    else if (ntoks==4 && strcmp(cmd, "div")==0) handle_div_cmd(tokens, ntoks, vs);
    else if (ntoks==2 && strcmp(cmd, "mod")==0) handle_mod_cmd(tokens, ntoks, vs);
    else if (ntoks==3 && strcmp(cmd, "rename")==0) handle_rename_cmd(tokens, ntoks, vs);
    else if (ntoks==1 && strcmp(cmd, "purge")==0) handle_purge_cmd(vs);
    else if (ntoks==1 && strcmp(cmd, "list")==0) handle_list_cmd(vs);
    else if (ntoks==2 && strcmp(cmd, "del")==0) handle_del_cmd(tokens, ntoks, vs);
    else if (ntoks==3 && strcmp(cmd, "loop")==0) handle_loop_cmd(tokens, ntoks, vs);
    else if (ntoks==4 && strcmp(cmd, "str")==0) handle_str_cmd(tokens, ntoks, vs);
    else if (ntoks==3 && strcmp(cmd, "ferm")==0 && strcmp(tokens[1], "run")==0) handle_ferm_run_cmd(tokens, ntoks, vs, username_ref);
    else if (ntoks==1 && strcmp(cmd, "exit")==0) {
        vs_free(vs);
        printf("Exiting...\n");
        exit(0);
    } else if (strcmp(cmd,"reset")==0) {
        puts("<SyntaxError>:Invalid reset command");
    } else {
        // command allowed but not matched exactly
        puts("<SyntaxError>:Invalid usage or wrong args");
    }
}

char *read_username_file() {
    FILE *f = fopen("authentication.fermlog", "r");
    if (!f) return NULL;
    char buf[LINE_BUF];
    if (!fgets(buf, sizeof(buf), f)) { fclose(f); return NULL; }
    trim_newline(buf);
    fclose(f);
    // split on ':' and take right side
    char *p = strchr(buf, ':');
    if (!p) return NULL;
    p++; while (*p && isspace((unsigned char)*p)) p++;
    return strdup(p);
}

char *read_password_file() {
    FILE *f = fopen("password.fermlog", "r");
    if (!f) return NULL;
    char buf[LINE_BUF];
    if (!fgets(buf, sizeof(buf), f)) { fclose(f); return NULL; }
    trim_newline(buf);
    fclose(f);
    char *p = strchr(buf, ':');
    if (!p) return NULL;
    p++; while (*p && isspace((unsigned char)*p)) p++;
    return strdup(p);
}

void password_flow() {
    char *pswd = read_password_file();
    if (!pswd) {
        // set new
        char buf[LINE_BUF];
        printf("Set a new password : ");
        if (!fgets(buf, sizeof(buf), stdin)) exit(1);
        trim_newline(buf);
        FILE *f = fopen("password.fermlog", "w");
        if (!f) { perror("fopen"); exit(1); }
        fprintf(f, "Password : %s\n", buf);
        fclose(f);
        free(pswd);
        // return to allow main to continue; the Python version calls main() here
        return;
    }
    int tries = 0;
    char attempt[LINE_BUF];
    while (tries < MAX_TRIES) {
        printf("Password : ");
        if (!fgets(attempt, sizeof(attempt), stdin)) exit(1);
        trim_newline(attempt);
        if (strcmp(attempt, pswd)==0) {
            free(pswd);
            return;
        }
        tries++;
        if (tries >= MAX_TRIES) {
            printf("Maximum number of tries reached and the running module has been locked for 30 minutes. Please try again after 30 mins.\n");
            // Python code used time.sleep(900) (15 minutes), message says 30 — we keep the sleep used
            sleep_seconds(900);
            exit(1);
        } else {
            printf("Wrong Passsword! Tries Left : %d\n", MAX_TRIES - tries);
        }
    }
    free(pswd);
}

int main_loop() {
    VarStore vs;
    vs_init(&vs);

    char *username = read_username_file();
    if (username) {
        if (strlen(username) == 0) {
            free(username);
            username = NULL;
        } else {
            printf("Logged in as @%s\n", username);
        }
    }
    if (!username) {
        char buf[LINE_BUF];
        printf("Set your new username: ");
        if (!fgets(buf, sizeof(buf), stdin)) return 1;
        trim_newline(buf);
        username = strdup(buf);
        FILE *f = fopen("authentication.fermlog", "w");
        if (f) {
            fprintf(f, "username : %s\n", username);
            fclose(f);
        }
    }

    printf("Creating Environment...\n");
    sleep_seconds(1);

    char line[LINE_BUF];
    while (1) {
        printf(">>> %s@fermion ~$ ", username);
        if (!fgets(line, sizeof(line), stdin)) {
            puts("");
            break;
        }
        trim_newline(line);
        int ntoks;
        char **toks = split_tokens(line, &ntoks);
        process_tokens(toks, ntoks, &vs, &username);
        free_tokens(toks, ntoks);
    }

    free(username);
    vs_free(&vs);
    return 0;
}

int main(void) {
    // Optional clear (python had clear() but not used)
    // clear_screen();

    printf("Welcome to Fermion\n");
    password_flow();
    // If password_flow created the password file and returned, we continue (Python called main())
    // If password_flow validated the password it returned too.
    return main_loop();
}
