function loadingbar(percentage) {
  resetBar();

  if (percentage < 50) {
    percentage = 100 - percentage;
    $(".result-c").addClass("bg-red-400");
    $(".result-w").addClass("bg-red-500");
    $("<p id='result-p'>False</p>").appendTo(".result-a");
  } else {
    $(".result-c").addClass("bg-green-400");
    $(".result-w").addClass("bg-green-500");
    $("<p id='result-p'>True</p>").appendTo(".result-a");
  }

  $(".result-c").width(percentage + "%");
  $(".result-w").width(100 - percentage + "%");
  $(`<p id="result-pp" >${percentage}%</p>`).appendTo(".result-c");
}

//!Reset the bar
function resetBar() {
  $(".result-c").removeClass("bg-red-400");
  $(".result-w").removeClass("bg-red-500");
  $(".result-c").removeClass("bg-green-400");
  $(".result-w").removeClass("bg-green-500");
  $("#result-p").remove();
  $("#result-pp").remove();
}

//!takes input [[0.4213]] returns 42
function parseInput(res) {
  return parseFloat(res.substring(2).slice(0, -2)).toFixed(2) * 100;
}

async function onTestChange() {
  let key = window.event.keyCode;
  let string = $(".fact-input").val();
  //! If the user has pressed enter
  if (key === 13) {
    try {
      const res = await fetch("http://127.0.0.1:5000/create/", {
        method: "POST",
        body: JSON.stringify({
          string,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await res.json();
      loadingbar(parseInput(data));
    } catch (err) {
      console.log(err);
    }
  }
}

loadingbar(100);

$("#js-show").on("click", function () {
  if ($(".js-table").hasClass("hidden")) $(".js-table").removeClass("hidden");
  else $(".js-table").addClass("hidden");
});
