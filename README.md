# fedora Stewardship SIG

Data and code in this git repository is either released into the Public Domain,
or licensed under the terms of the **Unlicense** license text contained in the
`LICENSE` file, whichever is applicable wherever you are.

For more information, look into the `docs` folder or go to
<https://fedora-stewardship.github.io>.

To build and view documentation locally, install `ruby` and `bundler`, and then
execute `bundle install` or `bundle update`, which will download and build all
dependencies into the `vendor` folder. Once that's done, you can use this
command to build a live preview of the docs:

```
bundle exec jekyll serve --watch --livereload
```

