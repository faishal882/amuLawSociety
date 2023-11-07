document.addEventListener('w-formset:ready', function(event) {
  console.log("I WORKED");
  console.info('ready', event);
});

document.addEventListener('w-formset:added', function(event) {
  console.log("I ADDED");
  console.info('added', event);
});

document.addEventListener('w-formset:removed', function(event) {
  console.log("I REMOVED");
  console.info('removed', event);
});
