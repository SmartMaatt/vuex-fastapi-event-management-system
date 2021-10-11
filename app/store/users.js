export const state = () => ({
    data: []
})

export const mutations = {
    storeData: (store, data) => {
        store.data = data
    }
}
