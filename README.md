# Hi, I'm Nicholas Sobchak

**Computer science student at UMBC · C++ systems & backend development · Graduating May 2027**

I build native engines, backend APIs, and the web applications around them. My work spans C++ data structures and concurrency, Java services, and AWS infrastructure, with an emphasis on testing and secure handling of user data.

[Portfolio](https://nickczak.github.io/portfolio/) · [Résumé](https://github.com/nickczak/resume/blob/main/mainC.pdf) · [LinkedIn](https://www.linkedin.com/in/nicholas-sobchak-b4aa2a329/) · [Email](mailto:nlsobchak@gmail.com)

## Experience

**Founding Software Developer at ZipTip** · December 2025–present

Building backend services for a tipping platform using AWS Lambda, API Gateway, DynamoDB, and Cognito. My work includes authentication, scan-to-account routing, pytest coverage, and AWS SAM deployment pipelines with OIDC authentication and rollback support.

## Selected projects

### [QuickQuill — Dictionary & Spell Checker](https://github.com/nickczak/QuickQuill-Dictionary-SpellChecker)

A full-stack dictionary application powered by a C++17 engine and a dictionary of roughly 1.28 million words.

- Implemented trie-based autocomplete and spelling suggestions, with a synchronized LRU cache and thread-local SQLite connections.
- Connected the native engine to a Spring Boot REST API through Java's Foreign Function & Memory API and a C interface.
- Added Catch2 tests for the engine and concurrent lookups; built an Angular frontend and Docker deployment.

**C++17 · Java · Spring Boot · SQLite · PostgreSQL · Angular · Docker**

### [On The Money — Personal Finance Tracker](https://github.com/nickczak/OnTheMoney-Finance-Tracker)

A finance application combining bank-account connections, transaction tracking, and portfolio growth projections.

- Integrated a C++ Monte Carlo engine with Spring Boot to run 10,000 simulations per projection request.
- Connected accounts and synchronized transactions through Plaid, keeping access tokens encrypted in the backend with AES-GCM.
- Built a React progressive web app backed by PostgreSQL, with Catch2 tests for simulation calculations and edge cases.

**C++17 · Java · Spring Boot · PostgreSQL · React · TypeScript · Docker**

## Tools I work with

| Area | Technologies |
| --- | --- |
| Languages | C++, Java, Python, SQL, TypeScript, JavaScript |
| Backend & data | Spring Boot, PostgreSQL, SQLite, DynamoDB |
| Cloud & delivery | AWS Lambda, API Gateway, Cognito, SAM, Docker, GitHub Actions |
| Development & testing | Linux, Git, CMake, Valgrind, Catch2, pytest, JUnit |

## Beyond the code

I play ice hockey at UMBC and serve as a section leader in a community orchestra.

Interested in my work? [Get in touch](mailto:nlsobchak@gmail.com).
