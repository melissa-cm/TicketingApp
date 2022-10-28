<template>
    <button id="MyDelButton" :style="{ background, color }">
        Delete project
    </button>
</template>

<script>
export default {
    props: {color: {type: String}, background: {type: String}, disabled: {type: Boolean}}
} 
</script>

<style scoped>
button {
    /* background: white;
    color: white;
    border-color: black;
    border-radius: 5px;
    padding: 10px 10px; */
    font-size: 14px;
    cursor: pointer;
    position: absolute;
 }

 button:hover {
    filter: brightness(125%);
 }
</style>