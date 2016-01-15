import Ember from 'ember';

export default Ember.Controller.extend({
    isShowingModal: false,
    actions: {
        generateList: function () {
            // Here we will instantiate a fake model and jam stuff into it
        },
        createRecipe: function() {
            var existing = this.model.get('firstObject');
            var recipe = this.store.createRecord('recipe', {
                'name': this.get('inputName'),
                'user': existing.get('user'),
            });
            recipe.save().then(function(){}, function(){ alert('failure'); });
            this.send('toggleModal');
        },
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
    inputName: '',
});
