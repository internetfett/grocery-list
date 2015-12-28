import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  setTitle: function(title) {
    var renderer = this.container.lookup('renderer:-dom');
    if(renderer) {
        Ember.set(renderer, '_dom.document.title', title);
    } else {
        document.title = title;
    }
  },
});

Router.map(function() {
  this.route('checklists');
  this.route('checklist', { path: '/checklist/:id' });
});

export default Router;

Ember.Route.reopen({
  init: function() {
    if(this.title) {
      this.router.setTitle(this.title);
    }
    this._super.apply(this, arguments);
  },
  /*setupController: function(controller, model) {
    this._super(controller, model);

    var route = this;
    var appController = this.controllerFor('application');

    if(this._appContextVars) {
      this._appContextVars.forEach(function(item) {
        appController.set(item, route.get(item));
      });
    }

    if(this._appContextModelAttrs) {
      this._appContextModelAttrs.forEach(function(item) {
        appController.set(item, model.get(route.get(item)));
      });
    }
  },*/
});
