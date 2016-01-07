import Ember from 'ember';

export default Ember.Controller.extend({
    sortedList: Ember.computed.sort('model.combined', '_combinedSort'),
    _combinedSort: ['status:asc', 'name:asc'],
    isShowingModal: false,
    actions: {
        createItem: function() {
            var item = this.store.createRecord('checklist-item', {
                'name': this.get('name'),
                'unit': 'unit',//this.get('units'),
                'amount': 1,//this.get('amount'),
            });
            item.set('checklist', this.model);
            item.save().then(function(){}, function(){ alert('failure'); });
            this.send('toggleModal');
        },
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
});
