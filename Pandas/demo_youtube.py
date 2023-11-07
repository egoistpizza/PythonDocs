import pandas as pd

df = pd.read_csv("youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:10]

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df.head(50)[["likes","dislikes"]]

# 7- En çok görüntülenen video hangisidir ?
result = df[df["views"] == df["views"].max()]

# 8- En düşük görüntülenen video hangisidir?
result = df[df["views"] == df["views"].min()]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values("views",ascending=False).head(10)

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["title"].apply(len)
result = df["title_len"]

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df["tag_count"] = df["tags"].apply(lambda tag: len(tag.split("|")))
result = df["tag_count"]

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

def calcPopularity(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])
    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = calcPopularity(df)

# print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])

# print(result)
