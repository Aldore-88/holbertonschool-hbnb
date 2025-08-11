<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script>
  const dateInput = document.getElementById("customDate");
  const dateIcon = document.querySelector(".date-icon");

  // Initialize Flatpickr
  const fp = flatpickr(dateInput, {
    dateFormat: "F j, Y", // Example: August 9, 2025
  });

  // Open date picker when clicking icon
  dateIcon.addEventListener("click", () => {
    fp.open();
  });
</script>

