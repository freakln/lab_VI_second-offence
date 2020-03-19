query = """
query{
  search(query: "user:gvanrossum", type: REPOSITORY, first: 50 %s) {
    repositoryCount
    pageInfo {
      hasNextPage
      endCursor
    }   
    nodes {
      ... on Repository {
        name
        url
        stargazers{totalCount}
        watchers{totalCount}
        forkCount
        isFork
        commitComments{totalCount}
        releases{totalCount}
        createdAt
        primaryLanguage {
          name
        }
      }
    }
  }
  rateLimit {
    remaining
    resetAt
  }
}
    """