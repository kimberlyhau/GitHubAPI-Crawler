from github_api import GitHubAPI

def pull_repos(api):
    closed_source_llms_2022 = ['lamda']# ["gpt", "lambda","alexatm"]#"Claude", "Coral", "AlexaTM", "LaMDA", "PaLM"] #['gemini']
    closed_source_llms_2023 = ["alexa"]#,"coral","claude"]#"chatgpt",'lamda',"alexatm","palm","coral","claude"]"palm",
    llm_frameworks = ['langchain']#,'langchain','mlc%20llm']
    open_source_llms = ["llama", "gemma", "mistral","Vicuna","mixtral","StableLM"]# "Qwen", "phi3", "Phi-1.5", "RedPajama", "Orca",  "falcon", "starling", "DeepSeek", "MiniChat", "Marcoroni", "Nyxene", "Una%20Xaberius", "ShiningValiant", Vicuna, Stable Beluga, StableLM  

     # REMEMBER TO CHANGE
    created_date_from_list_2024 = ['2024-01-01', '2024-01-08', '2024-01-16', '2024-01-24', '2024-02-01', '2024-02-08', '2024-02-16', '2024-02-24', '2024-03-01', '2024-03-08', '2024-03-16', '2024-03-24', '2024-04-01', '2024-04-08', '2024-04-16', '2024-04-24', '2024-05-01', '2024-05-08', '2024-05-16', '2024-05-24', '2024-06-01', '2024-06-08', '2024-06-16', '2024-06-24']
    created_date_to_list_2024 = ['2024-01-07', '2024-01-15', '2024-01-23', '2024-01-31', '2024-02-07', '2024-02-15', '2024-02-23', '2024-02-29', '2024-03-07', '2024-03-15', '2024-03-23', '2024-03-31', '2024-04-07', '2024-04-15', '2024-04-23', '2024-04-30', '2024-05-07', '2024-05-15', '2024-05-23', '2024-05-31', '2024-06-07', '2024-06-15', '2024-06-23', '2024-06-30']
    created_date_from_list_2023 = ['2023-01-01', '2023-01-08', '2023-01-16', '2023-01-24', '2023-02-01', '2023-02-08', '2023-02-16', '2023-02-24', '2023-03-01', '2023-03-08', '2023-03-16', '2023-03-24', '2023-04-01', '2023-04-08', '2023-04-16', '2023-04-24', '2023-05-01', '2023-05-08', '2023-05-16', '2023-05-24', '2023-06-01', '2023-06-08', '2023-06-16', '2023-06-24', '2023-07-01', '2023-07-08', '2023-07-16', '2023-07-24', '2023-08-01', '2023-08-08', '2023-08-16', '2023-08-24', '2023-09-01', '2023-09-08', '2023-09-16', '2023-09-24', '2023-10-01', '2023-10-08', '2023-10-16', '2023-10-24', '2023-11-01', '2023-11-08', '2023-11-16', '2023-11-24', '2023-12-01', '2023-12-08', '2023-12-16', '2023-12-24']
    created_date_to_list_2023 = ['2023-01-07', '2023-01-15', '2023-01-23', '2023-01-31', '2023-02-07', '2023-02-15', '2023-02-23', '2023-02-28', '2023-03-07', '2023-03-15', '2023-03-23', '2023-03-31', '2023-04-07', '2023-04-15', '2023-04-23', '2023-04-30', '2023-05-07', '2023-05-15', '2023-05-23', '2023-05-31', '2023-06-07', '2023-06-15', '2023-06-23', '2023-06-30', '2023-07-07', '2023-07-15', '2023-07-23', '2023-07-31', '2023-08-07', '2023-08-15', '2023-08-23', '2023-08-31', '2023-09-07', '2023-09-15', '2023-09-23', '2023-09-30', '2023-10-07', '2023-10-15', '2023-10-23', '2023-10-31', '2023-11-07', '2023-11-15', '2023-11-23', '2023-11-30', '2023-12-07', '2023-12-15', '2023-12-23', '2023-12-31']
    created_date_from_list_2022 = ['2022-01-01', '2022-01-08', '2022-01-16', '2022-01-24', '2022-02-01', '2022-02-08', '2022-02-16', '2022-02-24', '2022-03-01', '2022-03-08', '2022-03-16', '2022-03-24', '2022-04-01', '2022-04-08', '2022-04-16', '2022-04-24', '2022-05-01', '2022-05-08', '2022-05-16', '2022-05-24', '2022-06-01', '2022-06-08', '2022-06-16', '2022-06-24', '2022-07-01', '2022-07-08', '2022-07-16', '2022-07-24', '2022-08-01', '2022-08-08', '2022-08-16', '2022-08-24', '2022-09-01', '2022-09-08', '2022-09-16', '2022-09-24', '2022-10-01', '2022-10-08', '2022-10-16', '2022-10-24', '2022-11-01', '2022-11-08', '2022-11-16', '2022-11-24', '2022-12-01', '2022-12-08', '2022-12-16', '2022-12-24']
    created_date_to_list_2022 = ['2022-01-07', '2022-01-15', '2022-01-23', '2022-01-31', '2022-02-07', '2022-02-15', '2022-02-23', '2022-02-28', '2022-03-07', '2022-03-15', '2022-03-23', '2022-03-31', '2022-04-07', '2022-04-15', '2022-04-23', '2022-04-30', '2022-05-07', '2022-05-15', '2022-05-23', '2022-05-31', '2022-06-07', '2022-06-15', '2022-06-23', '2022-06-30', '2022-07-07', '2022-07-15', '2022-07-23', '2022-07-31', '2022-08-07', '2022-08-15', '2022-08-23', '2022-08-31', '2022-09-07', '2022-09-15', '2022-09-23', '2022-09-30', '2022-10-07', '2022-10-15', '2022-10-23', '2022-10-31', '2022-11-07', '2022-11-15', '2022-11-23', '2022-11-30', '2022-12-07', '2022-12-15', '2022-12-23', '2022-12-31']
    
    for query in open_source_llms:
        sum_repos = 0
        sum_code = 0
        sum_issues = 0
        sum_total = 0
        print(query)
        fmeta= open(query+"_meta_2024.txt","w+")     
        for i in range(0,24):
            created_date_from = created_date_from_list_2024[i]
            created_date_to = created_date_to_list_2024[i]
            print("from: "+created_date_from)
            print("to: "+created_date_to)
            fmeta.write("from: "+created_date_from+"\n")
            fmeta.write("to: "+created_date_to+"\n")
            res_repos = api.get_repo(query,created_date_from,created_date_to, 0)
            res_code = api.get_repo(query,created_date_from,created_date_to, 1)
            res_issues = api.get_repo(query,created_date_from,created_date_to, 2)

            print("from: "+created_date_from)
            print("to: "+created_date_to)
            print("Repo search")
            print(res_repos['total_count'])
            print(len(res_repos['items']))
            fmeta.write("Repo search\n"+str(res_repos['total_count'])+"\n"+str(len(res_repos['items']))+"\n")
            repos = [res_repos['items'][i]['url'] for i in range(len(res_repos['items']))]
            
            f= open(query+'_'+created_date_from+"_repos.txt","w+")
            for r in repos:
                f.write(r+"\n")
            f.close()
            
            sum_repos += res_repos['total_count']
            
            print("Code search")
            print(res_code['total_count'])
            print(len(res_code['items']))
            fmeta.write("Code search\n"+str(res_code['total_count'])+"\n"+str(len(res_code['items']))+"\n")
            code = [res_code['items'][i]['url'] for i in range(len(res_code['items']))]
            """
            f= open(query+'_'+created_date_from+"_code.txt","w+")
            for r in code:
                f.write(r+"\n")
            f.close()
            sum_code += res_code['total_count']
            """
            print("Issues search")
            print(res_issues['total_count'])
            print(len(res_issues['items']))
            fmeta.write("Issues search\n"+str(res_issues['total_count'])+"\n"+str(len(res_issues['items']))+"\n")
            issues = [res_issues['items'][i]['repository_url'] for i in range(len(res_issues['items']))]
            
            f= open(query+'_'+created_date_from+"_issues.txt","w+")
            for r in issues:
                f.write(r+"\n")
            f.close()
            
            sum_issues += res_issues['total_count']

            urls = set(repos+code+issues)
            print("Total number")
            print(len(urls))
            fmeta.write("Total number\n"+str(len(urls))+"\n")
            
            f= open(query+'_'+created_date_from+".txt","w+")
            for url in urls:
                f.write(url+"\n")
            f.close()
            
            sum_total= sum_total+len(urls)
            print("sum repos "+str(sum_repos))
            print("sum code "+str(sum_code))
            print("sum issues "+str(sum_issues))
            print("sum total "+str(sum_total))
            fmeta.write("sum repos\n"+str(sum_repos)+"\n")
            fmeta.write("sum code\n"+str(sum_code)+"\n")
            fmeta.write("sum issues\n"+str(sum_issues)+"\n")
            fmeta.write("sum total\n"+str(sum_total)+"\n")
            
        fmeta.close()
    

if __name__ == "__main__":
    api = GitHubAPI()
    # # query github api with URL https://api.github.com/repos/jquery/jquery/pulls/4406/commits
    #     # res = api.request("repos/jquery/jquery/pulls/4406/commits")
    #     #

    # query issue/pr timeline
    #  api doc: https://developer.github.com/v3/issues/timeline/#list-timeline-events-for-an-issue
    # the following query the events for https://github.com/jquery/jquery/pull/4406/
    # events = api.get_issue_pr_timeline("jquery/jquery", 4406)

    pull_repos(api)
    #Search repos
    # dict_keys(['total_count', 'incomplete_results', 'items'])
    # items is list of dicts
    """
    dict_keys(['id', 'node_id', 'name', 'full_name', 'private', 'owner', 'html_url', 
    'description', 'fork', 'url', 'forks_url', 'keys_url', 'collaborators_url', 
    'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 
    'branches_url', 'tags_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 
    'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 
    'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 
    'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 
    'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 
    'labels_url', 'releases_url', 'deployments_url', 'created_at', 'updated_at', 'pushed_at', 
    'git_url', 'ssh_url', 'clone_url', 'svn_url', 'homepage', 'size', 'stargazers_count', 
    'watchers_count', 'language', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 
    'has_pages', 'has_discussions', 'forks_count', 'mirror_url', 'archived', 'disabled', 
    'open_issues_count', 'license', 'allow_forking', 'is_template', 'web_commit_signoff_required', 
    'topics', 'visibility', 'forks', 'open_issues', 'watchers', 'default_branch', 'permissions', 'score'])
    """
    """
    gpt - nov 2022
    - 2022: monthly
    claude - march 2023
    - 2023: 2 weeks
    - 2024: 2024 jan over 1000
    coral - 2023 december over 1000
    - 2023: 2 weeks
    - 2024: 1 week
    alexatm - 2022
    - 2022: monthly
    - 2023: 2 months
    gemini - march 2023
    - 2023: 1 week
    - 2024: 1 week
    lamda - 2021
    - 2022: month
    - 2023: 2 weeks
    - 2024: 2 weeks
    palm - april 2022
    - 2022: 2 weeks
    - 2023: 2 weeks
    - 2024: 2 weeks
    """
    