import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('checklists');
  this.route('checklist', { path: '/checklist/:id' });
});

export default Router;
