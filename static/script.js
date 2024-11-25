// Initialize animation on scroll
AOS.init({
    duration: 3000,
    offset: 120,
  });
  
  // Slider Functionality for Rotating Images
  function initializeSlider(slider) {
    const time = slider.dataset.sheetTime || 3000;
    const inputs = slider.querySelectorAll("input");
    let index = 0;
    let intervalId;
  
    function updateInputState() {
      inputs[index].checked = false;
      index = (index + 1) % inputs.length;
      inputs[index].checked = true;
    }
  
    function startInterval() {
      index = Array.from(inputs).findIndex((input) => input.checked) || 0;
      intervalId = setInterval(updateInputState, time);
    }
  
    const stopInterval = () => clearInterval(intervalId);
  
    startInterval();
  
    slider.addEventListener("mouseenter", stopInterval);
    slider.addEventListener("mouseleave", startInterval);
  }
  
  // Initialize sliders
  document.querySelectorAll("[data-sheet-time]").forEach(initializeSlider);  