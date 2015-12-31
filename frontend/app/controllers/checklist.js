import Ember from 'ember';

export default Ember.Controller.extend({
    sortedList: Ember.computed.sort('model.combined', '_combinedSort'),
    _combinedSort: ['status:asc', 'name:asc'],
    isShowingModal: false,
    actions: {
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
});
