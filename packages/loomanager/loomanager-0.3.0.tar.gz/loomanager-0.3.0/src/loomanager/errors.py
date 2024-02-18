from zenyx import printf

VERBOSE = False

def err(msg: str, hint: str = None) -> None:
    if VERBOSE:
        raise Exception(msg)
    
    printf.title("@!An error occured!$&")
    printf(f"@!💔 Error:$&\n  {msg}")
    if hint is not None:
        printf("\n💡 @!Hint:$&")
        printf("  ", "\n  ".join(hint.split("\n")), sep="")
        printf("\n")
    exit()