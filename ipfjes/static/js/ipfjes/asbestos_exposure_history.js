angular.module('opal.controllers').controller('AsbestosExposureHistoryCtrl', function(scope, step, episode){
    "use strict";
    if(_.isArray(scope.editing.asbestos_exposure_screening)){
      scope.editing.asbestos_exposure_screening = _.first(scope.editing.asbestos_exposure_screening);
    }
});
