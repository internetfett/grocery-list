import Ember from 'ember';

export default Ember.Controller.extend({
    sortedList: Ember.computed.sort('model.combined', '_combinedSort'),
    _combinedSort: ['status:asc', 'name:asc'],
    isShowingModal: false,
    actions: {
        createItem: function() {
            var item = this.store.createRecord('checklist-item', {
                'name': this.get('inputName'),
                'unit': this.get('inputUnit'),
                'amount': this.get('inputAmount'),
            });
            item.set('checklist', this.model);
            item.save().then(function(){}, function(){ alert('failure'); });
            this.send('toggleModal');
        },
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
    inputName: '', inputUnit: 'unit', inputAmount: 0.125,
    units: ['unit', 'cup', 'oz', 'lb', 'tsp', 'tbsp'],
    amounts: [
        {label: '1/8', value: 0.125},
        {label: '1/4', value: 0.25},
        {label: '1/2', value: 0.5},
        {label: '3/4', value: 0.75},
        {label: '1', value: 1},
        {label: '2', value: 2},
        {label: '3', value: 3},
        {label: '4', value: 4},
        {label: '5', value: 5},
        {label: '6', value: 6},
        {label: '7', value: 7},
        {label: '8', value: 8},
        {label: '9', value: 9},
        {label: '10', value: 10},
    ],
});
