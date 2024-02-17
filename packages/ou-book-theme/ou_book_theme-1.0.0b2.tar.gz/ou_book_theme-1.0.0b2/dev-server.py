#!/usr/bin/env python
from livereload import Server, shell

full_build = shell("jupyter-book build --all docs")
partial_build = shell("jupyter-book build docs")
npm_build = shell("npm run build")

shell("npm install")()
npm_build()
full_build()

server = Server()
server.watch("docs/**/*.md", partial_build)
server.watch("docs/**/*.yml", full_build)
server.watch("ou_book_theme/assets/**/*.*", npm_build)
server.watch("ou_book_theme/theme/**/*.*", full_build)
server.watch("ou_book_theme/**/*.py", full_build)
server.serve(root="docs/_build/html", port=8000)
