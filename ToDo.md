# ToDo

## Frontend

### Kyle
-   [ ] Set up useContext for user tracking (persist across refresh if time)
-   [ ] FE styling of received information


### David

-   [x] JWT Tokens
-   [x] Edit paper data
-   [ ] Axios calls for data with relationships (i.e. get user with topics {interests})

## Backend

### Evan

-   [ ] Services

    -   [ ] Connect to Arxiv
    -   [ ] Connect to OpenAI with Langchain
        -   [ ] Strip references from paper
        -   [ ] Chunk paper
        -   [ ] Generate chunk summaries
        -   [ ] Combine chunk summaries and summarize into short (200-500 words) and long summaries (1000-2000 words)

-   [ ] Update Papers table (ORM)

    -   [ ] Include Title, Authors, Published Date, Abstract, and Link

-   [ ] Update Routes to use Annotated and Query instead of the custom created schemas
-   [ ] Unit tests
-   [ ] Feed web scraper info into DB

### David