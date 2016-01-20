import OAuth2PasswordGrant from 'ember-simple-auth/authenticators/oauth2-password-grant';
import ENV from 'frontend/config/environment';

export default OAuth2PasswordGrant.extend({
    serverTokenEndpoint: ENV.APP.API_HOST + '/o/token/',
    serverTokenRevocationEndpoint: ENV.APP.API_HOST + '/o/revoke_token/',
    makeRequest: function(url, data) {
        data.client_id = ENV.APP.CLIENT_ID;
        data.client_secret = 'nEUTb7AI49QTEngrnCT5HtEkTY4sPYbKrN0OJzXHvEYyPj6eec8SRKGVTlKtELyZT5h0LPKOWhuIUt480umtr8UfWTdTbLtl6nJAy6QwYOmMQF5x36VdktiSBiF3lUqe';
        return this._super(url, data);
    }
});
