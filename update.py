import os

blog = os.listdir('blogposts')

l = []
for i in blog:
	if i.split(".")[1] == "html":
		l.append(i)


js = """ 
let posts = {}

console.log(posts)

blogcontent = document.querySelector("#add-post")

posts.forEach( (post) => {{
	let newpost = document.createElement('div')
	let posttitle = post.split('.')[0]
	newpost.className = 'card'
	newpost.innerHTML = `<div class="tags">
                <p>${{posttitle}}</p>
                </div>
                <a href="blogposts/${{post}}" style="text-transform: capitalize;">${{posttitle}}</a>`
    blogcontent.appendChild(newpost)
}})
""".format(str(l))


with open('posts.js', 'w') as filewrite:
	filewrite.write(js)