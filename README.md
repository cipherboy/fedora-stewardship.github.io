# fedora Stewardship SIG

Data and code in this git repository is either released into the Public Domain,
or licensed under the terms of the **Unlicense** license text contained in the
`LICENSE` file, whichever is applicable wherever you are.

For more information, read the files in `_pages`, or view the rendered docs at
<https://fedora-stewardship.github.io>.

### Rendering and viewing pages locally

To build and view documentation locally, install `ruby` and `bundler`, and then
execute `bundle install` or `bundle update`, which will download and build all
dependencies into the `vendor` folder. Once that's done, you can use this
command to build a live preview of the docs, which will then be available on
<http://localhost:4000> by default.

```
bundle exec jekyll serve --watch --livereload
```

**NOTE**: Do not run this with the `--watch` flag while updating the generated
pages and images with the `update` script - it will lead to problems and broken
images.

When updating outdated documentation, please update the `updated: DATE` header
in markdown files accordingly.

### Automatically updating generated content

The report, PR report, overview, and backlog pages are automatically generated
from rawhide repository data, the list of packages currently maintained by this
SIG, open pull requests on SIG package repositories, and the curated data in
`data/events.json`.

To automatically check for new data, and update the pages accordingly, just run
the `./update` script. It has only a few requirements:

- `dnf`, `dnf-tools` and `fedora-repos-rawhide`
- `python >= 3.5`
- `jinja2`, `pandas`, `prettytable`, `requests`, `rpm` python3 modules

**NOTE**: @decathorpe has a cron job that does this automatically.
