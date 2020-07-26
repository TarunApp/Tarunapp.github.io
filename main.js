let pchange = document.getElementById("main-heading")

fetch("https://type.fit/api/quotes")
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {


        let e = []



        for (var i = 0; i < data.length; i++) {

            if (data[i].author != null) {
                e.push({ "text": data[i].text, "author": data[i].author })
            }
        }

        let rand = Math.floor(Math.random() * 1547)
        let k = rand;

        // console.log(e)
        console.log(e.length)

        console.log(rand)
        console.log(e[rand])
        console.log(` ${e[rand].text} - ${e[rand].author} `)
        pchange.innerHTML = `<h1> ${e[rand].text} - ${e[rand].author} </h1>`
        pchange.id = "main-heading"
    });