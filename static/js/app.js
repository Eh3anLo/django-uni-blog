document.addEventListener("DOMContentLoaded", function() {
    // Select all <code> elements with the class 'code'
    const codeElements = document.querySelectorAll('code.code');

    codeElements.forEach(codeElement => {
        // Create a new <pre> element
        const preElement = document.createElement('pre');

        // Append the <code> element to the new <pre> element
        preElement.appendChild(codeElement.cloneNode(true));

        // Replace the old <code> element with the new <pre> element in the DOM
        codeElement.parentNode.replaceChild(preElement, codeElement);
    });
});
