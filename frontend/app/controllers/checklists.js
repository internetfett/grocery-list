import Ember from 'ember';

export default Ember.Controller.extend({
    sortProperties: ['name:asc'],
    sortedList: Ember.computed.sort('model', 'sortProperties'),
    isShowingModal: false,
    actions: {
        createChecklist: function() {
            // TODO: Replace with Oauth2 User
            var existing = this.model.get('firstObject');
            var checklist = this.store.createRecord('checklist', {
                'name': this.get('inputName'),
                'user': existing.get('user'),
            });
            checklist.save().then(function(){}, function(){ alert('failure'); });
            this.send('toggleModal');
        },
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
    inputName: '',
});
