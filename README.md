# GetName

Get cat/dog/superhero/supervillain names.

I just combine [@sindresorhus][]'s four staffs into this one.

* [cat-names][]
* [dog-names][]
* [superheroes][]
* [supervillains][]

## Usage

Use `getname -h` to get help message about each usage.

    Usage: getname [OPTIONS] COMMAND [ARGS]...

        Get popular cat/dog/superhero/supervillain names.

        Options:
            -v, --version  Show the version and exit.
            -h, --help     Show this message and exit.

        Commands:
            cat      Get popular cat names.
            dog      Get popular dog names.
            hero     Get superhero names.
            villain  Get supervillain names.

Use `getname cat/dog/hero/villain -h` to get help message about the specified type.

## Credits

All the glories should belong to [@sindresorhus][], I just port it to python :)

## License

MIT.

[@sindresorhus]: https://github.com/sindresorhus
[dog-names]: https://github.com/sindresorhus/dog-names
[cat-names]: https://github.com/sindresorhus/cat-names
[superheroes]: https://github.com/sindresorhus/superheroes
[supervillains]: https://github.com/sindresorhus/supervillains