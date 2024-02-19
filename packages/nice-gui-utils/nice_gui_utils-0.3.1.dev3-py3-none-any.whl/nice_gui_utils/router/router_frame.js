export default {
    template: "<div><slot></slot></div>",
    mounted() {
        window.addEventListener("popstate", (event) => {
            if (event.state?.page) {
                this.$emit("open", event.state.page);
            }
        });
        const connectInterval = setInterval(async () => {
            if (window.socket.id === undefined)
                return;
            this.$emit("open", window.location.pathname);
            clearInterval(connectInterval);
        }, this.checkInterval);
    },
    props: {
        checkInterval: Number
    },
    methods: {
        updateHistory(path) {
            if (window.location.pathname !== path) {
                history.pushState({page: path}, "", path);
            }
        }
    }
};