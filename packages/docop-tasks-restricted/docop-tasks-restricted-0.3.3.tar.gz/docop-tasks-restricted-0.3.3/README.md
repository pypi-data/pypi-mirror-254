This package contains packaged tasks for Docop.

The tasks use code that has fairly restrictive licensing for commercial use.

In particular, this package may contain code licensed under AGPL.

Be sure to respect the licenses.

For packaged tasks with more permissive licenses, see: https://github.com/koodaamo/docop-tasks-restricted

## html2text task

Extract plain text content of the HTML string.

Expects HTML text in the `html` field of document.
Output document will have following fields set:
  - `text` field containing the plain text content of the HTML
  - `fingerprint` generated from the text field for e.g. detecting changes
  - `modified` field indicating when text was changed, based on fingerprint, in HTTP Last-Modified format