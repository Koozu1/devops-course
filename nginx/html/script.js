function sendRequest() {
  fetch("/request")
    .then(async (response) => {
      if (response.status === 503) {
        document.getElementById("responseArea").value =
          "Service(s) unavailable.";
        return;
      }
      if (response) {
        document.getElementById("responseArea").value = await response.text();
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
