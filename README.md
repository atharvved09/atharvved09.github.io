# Atharv's Portfolio & Genetic Drift Lab

This repository hosts my personal portfolio and interactive simulations, available at [atharvved09.github.io](https://atharvved09.github.io/).

## Structure

- **`index.md`**: The main homepage. It uses a custom layout to display a grid of projects.
- **`_data/projects.yml`**: Contains the metadata for all displayed projects. **Do not edit this manually** if you plan to use the update script, as it will be overwritten.
- **`scripts/update_portfolio.py`**: A Python script to fetch repository data from GitHub and update `_data/projects.yml`.
- **`_layouts/default.html`**: The main page template (from the Cayman theme).
- **`assets/css/`**: Custom styles.

## How to Update

### Adding a New Project
1.  Open `scripts/update_portfolio.py`.
2.  Add the exact repository name to the `INCLUDE_REPOS` list.
3.  Run the update script:
    ```bash
    python3 scripts/update_portfolio.py
    ```
    *(Note: Requires `requests` and `pyyaml` libraries: `pip install requests pyyaml`)*

### Updating Content
-   To change the **Bio/About Me** section, edit `index.md`.
-   To change **Project Descriptions**, you can either:
    -   Update the description on GitHub (the script fetches this).
    -   Modify the `generate_summary` function in `scripts/update_portfolio.py` for custom AI-like summaries.

## Local Development

1.  Install Bundler and Jekyll:
    ```bash
    gem install bundler
    bundle install
    ```
2.  Run the server:
    ```bash
    bundle exec jekyll serve
    ```