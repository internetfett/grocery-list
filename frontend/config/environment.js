/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'frontend',
    environment: environment,
    rootURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
    ENV.APP.API_HOST = 'http://localhost:8000';
    ENV.APP.CLIENT_ID = '8RIA7ouqSum8JFwA3cLi0ZTbjPPdhxImRzFk4GyM';
    ENV.APP.CLIENT_SECRET = 'nEUTb7AI49QTEngrnCT5HtEkTY4sPYbKrN0OJzXHvEYyPj6eec8SRKGVTlKtELyZT5h0LPKOWhuIUt480umtr8UfWTdTbLtl6nJAy6QwYOmMQF5x36VdktiSBiF3lUqe';
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.rootURL = '/';
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {
    ENV.rootURL = '/grocerylist/';
    ENV.APP.API_HOST = 'http://internetfett.pythonanywhere.com';
    ENV.APP.CLIENT_ID = 'fytW0vpFBiH862Gcn3bY227NKhHPxanR6qUajttt';
    ENV.APP.CLIENT_SECRET = 'GdE3w1XTnO71tzYGKTcC4Ne5KyPuXC9dFiAwYjTmpg7y0ZroAI6mK4ie3rYXkKrqPeCBFVRdm7CVIJ6CjRVRZQrsrgmgXEo8M5qypkopCFBS00jTlsNoocAkMaspeG42';
  }

  return ENV;
};
