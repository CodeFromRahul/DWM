def page_rank(links,beta=0.8,iteration=2):
    N=len(links)
    ranks={page:1/N for page in links}

    # function for new link
    def calculate_rank(page):
        incoming_links=[source for source in links if page in links[source]]
        rank_sum =sum(ranks[source]/len(links[source]) for source in incoming_links)

        return (1-beta)+beta*rank_sum

    print(f"Iteration 0,{ranks}")

    for i in range(1,iteration+1):
        new_ranks={}
    
    for page in links:
        new_ranks[page]= calculate_rank(page)

    ranks=new_ranks

    print(f"Iteration {i}:{ranks}")
    
    # final 
    
    print("\nFinal pagerank values:")
    for page,rank in ranks.items():
        print(f"page{page}:{rank}")

    def get_user_input():
        num_pages=int(input("Enter the number of pages :"))
        links={}

        for i in range(num_pages):
            page=input("Enter page {i+1} name:")
            outgoing=input(f"Enter the putgoin links from {page}(comma-separated):").split(',')
            links[page]=[links.strip() for link in outgoing if links.strip()!='']
            return links
        
    if _name_ =="_main_":
        links =get_user_input()
        page_rank(links)
