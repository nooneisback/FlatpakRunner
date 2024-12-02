A simple python script to run your flatpaks from cli without typing out their full names. It matches the package name by default, or its id if the search pattern includes a dot.

A PKGBUILD file is included to install with makepkg.

```
Usage:flatrun <options> <packname> <runargs>
  Options:
    -h/--help        Prints out this page
    -f/--foreground  Tells flatrun not to append ">/dev/null 2>&1 &" to the end of the command. Use this to see the output.
    -l/--list        Lists flatpaks matching the search pattern without running them
  Packname: A search pattern for the package name/id. It will use the package name unless the search pattern includes a dot.
    Example:
      1 Some generic package  org.test.package
      2 Some other package    org.generic.something
      "flatrun generic" will run Some generic package
      "flatrun .generic" will run Some other package
  Runargs: will append these arguments to flatpak run packid
    Example:
      "flatrun -f packname arg1 arg2"
      Will run
      "sh -c flatpak run pack.id arg1 arg2"
```