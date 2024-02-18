
from newspaper import Article


def json_nltk2(url:str,html:str)->dict:
    article = Article(url)
    article.set_html(html)
    article.parse()
    article.nlp()
    _ = {
            "keywords": article.keywords,
            "summary": article.summary,
            "text": article.text,
            "title": article.title,
            "authors": article.authors,
            "publish_date": str(article.publish_date),
            "top_image": article.top_image,
            "meta_keywords": article.meta_keywords,
            "meta_description": article.meta_description,
            "meta_lang": article.meta_lang,
            "meta_favicon": article.meta_favicon,
            "canonical_link": article.canonical_link,
            "tags": list(article.tags),
            "movies": article.movies,
            "imgs": list(article.imgs),
        }
    return _
    