import OAuth2PasswordGrant from 'ember-simple-auth/authenticators/oauth2-password-grant';
import ENV from 'frontend/config/environment';

export default OAuth2PasswordGrant.extend({
    serverTokenEndpoint: ENV.APP.API_HOST + '/o/token/',
    serverTokenRevocationEndpoint: ENV.APP.API_HOST + '/o/revoke_token/',
    makeRequest: function(url, data) {
        data.client_id = ENV.APP.CLIENT_ID;
        data.client_secret = ENV.APP.CLIENT_SECRET;
        return this._super(url, data);
    }
});
