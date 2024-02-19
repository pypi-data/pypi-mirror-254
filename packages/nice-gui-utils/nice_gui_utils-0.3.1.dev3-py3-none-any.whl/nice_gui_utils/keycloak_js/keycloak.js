export default {
    template: "<div></div>",
    mounted() {
        this.keycloak = new Keycloak({
            url: this.url,
            realm: this.realm,
            clientId: this.clientId
        });

        this.keycloak.onTokenExpired = () => this.keycloak.updateToken();
        this.keycloak.init(this.initOptions);
    },
    methods: {
        token() {
            return this.keycloak.token;
        },
        refreshToken() {
            return this.keycloak.refreshToken;
        },
        authenticated() {
            return this.keycloak.authenticated;
        },
        login(options) {
            return this.keycloak.login(options);
        },
        logout(options) {
            return this.keycloak.logout(options);
        }
    },
    props: {
        url: String,
        realm: String,
        clientId: String,
        initOptions: Object
    }
};
