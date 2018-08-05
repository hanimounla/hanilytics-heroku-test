elements = document.getElementsByTagName("article")
count = 0
for (const element in elements) {
    if (elements.hasOwnProperty(element)) {
        const article = elements[element];
        if(count % 3 == 0)
            article.setAttribute("class","one_third first")
    }
    count++;
}
console.log(elements)