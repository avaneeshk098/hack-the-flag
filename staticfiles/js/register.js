window.onload = () => {
  [...document.getElementsByTagName('input')].forEach(element => {
      console.log(element)
      element.placeholder = " ";
  });
}