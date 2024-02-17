<script lang="ts">
  import { type CustomData, Markdown } from '@modelscope-gradio/compiled';
  import { afterUpdate, createEventDispatcher, onDestroy } from 'svelte';

  export let message = '';
  export let complete_message = false;
  export let flushing = false;
  export let theme = 'light';
  export let flushing_speed = 5;
  let display_message = '';
  let skip_message_positions: {
    start: number;
    end: number;
  }[] = [];
  let timeout: number;
  let i = 0;
  const flushing_end_tag = ':flushing-end';
  let last_flushing_end_index: number;

  $: _flushing_timeout =
    100 - (Math.max(Math.min(flushing_speed, 10), 1) * 100) / (10 - 1);

  const dispatch = createEventDispatcher<{
    flushed: string;
    update: void;
    custom: CustomData;
  }>();
  const skip_tag_reg = /:::llm-thinking|::llm-thinking-title|:flushing-end/g;

  function on_custom(tag: string, tag_index: number, value?: any) {
    dispatch('custom', { tag, tag_index, value });
  }

  $: if (flushing && complete_message && message === display_message) {
    dispatch('flushed', message);
  }

  $: {
    skip_message_positions = [
      ...Array.from(message.matchAll(skip_tag_reg)).map((match) => ({
        start: match.index!,
        end: match.index! + match[0].length,
      })),
    ];
  }

  $: if (message !== display_message) {
    // 每次message变化时清除前一个timeout
    clearTimeout(timeout);

    if (!flushing) {
      display_message = message;
    } else {
      last_flushing_end_index = message.lastIndexOf(flushing_end_tag);
      if (last_flushing_end_index !== -1) {
        const flushing_end_message = message.slice(
          0,
          last_flushing_end_index + flushing_end_tag.length
        );
        if (!display_message.startsWith(flushing_end_message)) {
          display_message = flushing_end_message;
          i = last_flushing_end_index;
        }
      }

      if (!message.startsWith(display_message)) {
        display_message = message.slice(0, i);
      }
      const position = skip_message_positions.find(
        (pos) => pos.start <= i && i < pos.end
      );
      // 重设 display_message 为空字符串
      timeout = setTimeout(() => {
        if (i < message.length) {
          if (position) {
            display_message += message.slice(position.start, position.end);
            i += position.end - position.start;
            return;
          }
          display_message += message.charAt(i);
          i++;
        }
      }, _flushing_timeout) as unknown as number;
    }
  }

  onDestroy(() => {
    clearTimeout(timeout);
  });
  afterUpdate(() => {
    dispatch('update');
  });
</script>

<Markdown
  {...$$restProps}
  elem_style="width: 100%"
  {last_flushing_end_index}
  end={!flushing || complete_message}
  flushing={flushing && (message !== display_message || !complete_message)}
  {theme}
  text={display_message}
  {on_custom}
/>
