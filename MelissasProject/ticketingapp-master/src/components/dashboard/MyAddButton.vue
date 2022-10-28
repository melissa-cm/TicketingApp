<template>
    <button v-bind="$attrs">
        Add new project
    </button>
</template>

<script>
 
</script>

<style scoped>
button {
    font-size: 14px;
    cursor: pointer;
    position: absolute;
 }

 button:hover {
    filter: brightness(125%);
 }
</style>
