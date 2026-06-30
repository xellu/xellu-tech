<script lang="ts">
    import { Select } from "bits-ui"; 
    import Icon from "./Icon.svelte";

    let {
        placeholder = "",
        type = "single",
        items = [],
        allowDeselect = false,
        value = $bindable()
    }: {
        placeholder: string,
        type?: "single" | "multiple",
        allowDeselect?: boolean
        items?: {value: string, label: string, disabled?: boolean}[],
        value?: any
    } = $props();
</script>
 
<Select.Root 
    type={type} 
    items={items} 
    allowDeselect={allowDeselect} 
    value={value}
    onValueChange={(v: any) => { value = v }}
>
  <Select.Trigger
    class="h-input w-full border-surface-800/80 bg-surface-950 data-placeholder:text-white/50 inline-flex touch-none select-none items-center border px-2.75 py-1 transition-colors"
    aria-label={placeholder}
  >
    <Select.Value placeholder={placeholder} />
  </Select.Trigger>
  <Select.Portal>
    <Select.Content
      class="focus-override border-surface-800/80 bg-surface-900 bg-[url(/mesh/diagonal-bt.png)] bg-repeat shadow-xl data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 outline-hidden z-50 max-h-96 max-h-[var(--bits-select-content-available-height)] w-[var(--bits-select-anchor-width)] min-w-[var(--bits-select-anchor-width)] select-none border p-3 data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1"
      sideOffset={10}
    >
      <Select.Viewport class="bg-surface-950 border border-surface-800/80">
        {#each items as item, i (i + item.value)}
          <Select.Item
            class="data-highlighted:bg-white data-highlighted:text-black outline-hidden data-disabled:opacity-50 flex h-10 w-full select-none items-center py-3 pl-5 pr-1.5 text-sm capitalize"
            value={item.value}
            label={item.label}
            disabled={item.disabled}
          >
            {#snippet children({ selected })}
              {item.label}
              {#if selected}
                <div class="ml-auto">
                  <Icon name="check" />
                </div>
              {/if}
            {/snippet}
          </Select.Item>
        {/each}
      </Select.Viewport>
    </Select.Content>
  </Select.Portal>
</Select.Root>