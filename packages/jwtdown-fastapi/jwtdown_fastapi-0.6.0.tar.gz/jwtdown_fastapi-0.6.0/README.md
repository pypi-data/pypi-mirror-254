# JWTdown for FastAPI

This is an easy-to-use authentication mechanism for FastAPI.

It draws inspiration from the tutorials found in the FastAPI
documentation.

Please read the
[documentation](https://jwtdown-fastapi.readthedocs.io/en/latest/intro.html)
to use this project.

## Developing

Development on this project is limited to employees, contractors, and students
of Galvanize, Inc.

When a new version of FastAPI is released:

1. Review the `MINIMUM_VERSION` in `update_fastapi_versions.py` and bump it
   as necessary
1. Run the `update_fastapi_versions.py`
1. Run `poetry update`
1. Add and commit the changes to:
   * `pyproject.toml`
   * `.tox-ci.yml`
   * `poetry.lock`

If all three of those things didn't change, check what you're doing.
