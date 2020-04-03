query = """
query{  
    user(login: "gvanrossum") {
            repositories(first: 50,isFork:false %s ) { 
      totalCount
      pageInfo {
          hasNextPage
          endCursor
      }
                       nodes {
                                ... on Repository {
                                  owner{login}
                                  name
                                  url
                                  stargazers{totalCount}
                                  watchers{totalCount}
                                  forkCount
                                  isFork
                                  commitComments{totalCount}
                                  releases{totalCount}
                                  createdAt
                                  primaryLanguage {name}
                                } 
                      }
      }
  }
}    
"""