document.addEventListener('DOMContentLoaded', function() {
    const line1Text = "Green energy";
    const line2Text = "made easy."; // Wrap the period in a span with a class
    const line1Element = document.getElementById('line1');
    const line2Element = document.getElementById('line2');
    let i = 0, j = 0;
  
    function typeWriter1() {
      if (i < line1Text.length) {
        line1Element.innerHTML += line1Text.charAt(i);
        i++;
        setTimeout(typeWriter1, 10); // Adjust typing speed
      } else {
        setTimeout(typeWriter2, 2450); // Small delay before starting line 2
      }
    }
  
    function typeWriter2() {
      if (j < line2Text.length) {
        line2Element.innerHTML += line2Text.charAt(j);
        j++;
        setTimeout(typeWriter2, 70); // Adjust typing speed for line 2
      }
    }
  
    typeWriter1(); // Start typing the first line
  });
  