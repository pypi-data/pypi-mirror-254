from zenyx import Arguments, printf
import loomanager.files as files
import loomanager.errors as errors
import loomanager.publish as publish
import sys
import os

args = Arguments(sys.argv)

def main():
    if args.tagged("INNER.cls"):
        printf.clear_screen()

    if len(args.normals) < 1:
        args.normals.append("git")

    if args.tagged("verbose"):
        errors.VERBOSE = True

    if args.normals[0] == "new":
        """Create new loom.toml"""
        files.new_config()

        if args.tagged("bat"):
            files.create_batch()

    if args.normals[0] == "update":
        """Update the module"""
        os.system("python -m pip install --updgrade loomanager")

    files.init()

    if args.normals[0] == "publish":
        """Commit and push to git"""
        publish.git()




if __name__ == "__main__":
    main()



