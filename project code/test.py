import matplotlib.pyplot as plt

def plots(articles):
    word_counts= [ [len(p) for p in article] for article in articles ]
    # print(word_counts)

    # plt.figure(figsize=(8,5))

    
    value=[]

    length_inlist=len(word_counts)
    print(length_inlist)

    for i in range(length_inlist):
        inds = [i+1]*len(word_counts[i])

        # for j in range(len(word_counts[i])):
        #     inds.append(i)
        print(inds)
        print(word_counts[i])
        plt.scatter(inds, word_counts[i], s=50, alpha=0.7, label=f"Article {i}")

    # print(inds)
    # print(value)

    #, s=100, alpha=0.6, label=f"Article {i}")

    

    plt.xlabel("Article number")
    plt.ylabel("Number of words in paragraph")
    plt.title("Paragraph word counts per article")
    # plt.xticks(range(1, len(articles)+1))
    # plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

articles = [
    ["this article one", "this article is good", "subscribe to it"],
    ["this article 2", "this article very good", "subscribe to this", "news the best here"],
    ["Breaking news: market hits all-time high", 
     "Experts say this could affect global economy", 
     "Login to read more", 
     "Subscribe to newsletter for updates"],
    ["Sports update: local team wins championship", 
     "Fans celebrate victory across city", 
     "Click here to see full highlights", 
     "Ticket sales for next season start soon"],
    ["Weather report: heavy rains expected tomorrow", 
     "Flood warnings issued in some regions", 
     "Stay safe and check official updates", 
     "Subscribe for weather alerts"],
    ["Tech article: new smartphone released", 
     "Features include high-resolution camera and AI assistant", 
     "Sign up to our newsletter for the latest tech news", 
     "Price and availability details inside"],
    ["Health tips: how to stay fit", 
     "Exercise regularly and maintain a balanced diet", 
     "Consult your doctor for personalized advice", 
     "Subscribe to our health newsletter"],
    ["Entertainment: upcoming movie releases", 
     "Blockbusters expected this summer", 
     "Login to watch trailers", 
     "Behind the scenes insights"]
]




plots(articles)