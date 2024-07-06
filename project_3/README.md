```markdown:project_3/README.md
# Workshop Demo Application - Let AI Be Your Docs

This is a demo application for the [Let AI Be Your Docs](https://github.com/mongodb-developer/vector-search-workshop) workshop.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is designed to demonstrate how AI can be used to generate and maintain documentation for a codebase. It is part of the "Let AI Be Your Docs" workshop.

## Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USER_NAME/project_3.git
    cd project_3
    ```

2. **Install dependencies:**

    ```bash
    pnpm install
    ```

3. **Set up environment variables:**

    Copy the `sample.env` file to `.env` and populate it with the necessary API keys and secrets.

    ```bash
    cp sample.env .env
    ```

4. **Create embeddings in MongoDB:**

    Run the `createEmbeddings.mjs` script to generate embeddings and store them in MongoDB.

    ```bash
    pnpm run embed
    ```

5. **Start the development server:**

    ```bash
    pnpm run dev
    ```

## Usage

To use the application, follow these steps:

1. **Run the application:**

    ```bash
    pnpm start
    ```

2. **Access the application:**

    Open your browser and navigate to `http://localhost:3000`.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. **Fork the repository:**

    Go to the repository on GitHub and click the "Fork" button.

2. **Clone your fork:**

    ```bash
    git clone https://github.com/YOUR_USER_NAME/project_3.git
    cd project_3
    ```

3. **Create a new branch:**

    ```bash
    git checkout -b my-feature-branch
    ```

4. **Make your changes and commit them:**

    ```bash
    git add .
    git commit -m "Description of my changes"
    ```

5. **Push your changes to your fork:**

    ```bash
    git push origin my-feature-branch
    ```

6. **Create a pull request:**

    Go to the repository on GitHub and click the "New pull request" button.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
