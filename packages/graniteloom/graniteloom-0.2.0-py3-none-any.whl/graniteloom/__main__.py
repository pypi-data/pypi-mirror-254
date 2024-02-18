from zenyx import Arguments, printf
import sys
import os


def get_token_repo_url(url: str, token: str) -> str:
    url = url.replace("https://github.com", "https://[< TOKEN >]@github.com")
    url = url.replace("[< TOKEN >]", token)
    return url


def clone_with_token(repo: str, token: str) -> None:
    repo = get_token_repo_url(repo, token)

    printf("\n@~Cloning with Access Token...$&\n")
    os.system(f"git clone {repo}")


def main():
    ARGS = Arguments(sys.argv)

    if ARGS.normals[0] == "help":
        printf.title("granite.")

        printf("\n@!Commands:$&")
        printf("  clone -> clone a repository with Github access token")
        printf("  workspace -> access workspace options")
        printf(
            "    login @~or$& join -> add remote origin by providing access token and url"
        )
        printf("    logout @~or$& quit -> remove remote origin")

        printf("\n@!Modifiers$&")
        printf('  -r "https://github.com/example/repo" -> specify the repo')
        printf('  -t "token" -> specify the token')

        printf("\n@!Options$&")
        printf("  --help -> Show this help menu")

        printf("\n")
        return

    url, token = "", ""

    if ARGS.normals[0] != "workspace" or ARGS.normals[1] not in ["logout", "quit"]:
        if ARGS.get_modifier_value("r"):
            url = ARGS.get_modifier_value("r")
        else:
            url = input("Repository URL: ")

        if ARGS.get_modifier_value("t"):
            token = ARGS.get_modifier_value("t")
        else:
            token = input("Github Access Token: ")

        if not url.startswith("https://github.com"):
            raise Exception("[Bad URL] Not Github URL")

    if ARGS.normals[0] == "clone":
        printf(url, token)
        clone_with_token(url, token)

    if ARGS.normals[0] != "workspace":
        return

    if ARGS.normals[1] in ["login", "join"]:
        repo = get_token_repo_url(url, token)

        if ARGS.get_modifier_value("t"):
            token = ARGS.get_modifier_value("t")
        else:
            token = input("Github Access Token: ")

        os.system("git remote rm origin")
        os.system(f"git remote add origin {repo}")

    if ARGS.normals[1] in ["logout", "quit"]:
        os.system("git remote rm origin")


if __name__ == "__main__":
    main()
