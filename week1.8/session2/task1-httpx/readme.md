
# Task 1 - Using httpx

We will use a simple source of web data: [HTTPbin](https://httpbin.io/json)

This provides synthetic data and a REST API, with no authentication, for testing code.

## Create a virtual environment

See slide on `Installing httpx CLI`

## Instal httpx

accidently downloaded a module wihout ebing in a virtual environment, how do i undo this

## Command-line use

We can fetch data for a single post from the API with

`httpx https://httpbin.io/json​`

Note the reply and identify:
- HTTP status code
- HTTP header
- Data (this format is called JSON, we will discuss it next)

## Other response codes

What is the difference if we request content that does not exist?

`httpx https://httpbin.io/jsoon​`
