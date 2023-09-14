document.addEventListener('DOMContentLoaded', fucntion(),{
	fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
	.then(reponse => reponse.json())
	.then(data => {
		const helloElement = document.getElementById('hello')
		helloElement.textContent = data.hello;
	})
	.catch(error => {
		console.error('There was an error fetching the greeting:', error);
        });
