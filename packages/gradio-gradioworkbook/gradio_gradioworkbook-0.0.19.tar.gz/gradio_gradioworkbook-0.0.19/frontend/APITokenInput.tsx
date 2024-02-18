import { memo, useState } from "react";
import {
  Alert,
  Anchor,
  Button,
  Flex,
  TextInput,
  createStyles,
} from "@mantine/core";

// Hacky, but we need to explicitly set mantine style here since gradio overrides
// with `.gradio-container-id a` specificity for anchor elements.
// See mantine-color-anchor definition in
// https://github.com/mantinedev/mantine/blob/d1f047bd523f8f36ab9edf3aff5f6c2948736c5a/packages/%40mantine/core/src/core/MantineProvider/global.css#L353
// TODO: Remove once overall style problem is fixed
const useStyles = createStyles((theme) => ({
  tokenLink: {
    color: `${
      theme.colorScheme === "dark" ? theme.colors.blue[4] : theme.primaryColor
    } !important`,
  },
}));

type Props = {
  onSetToken: (apiToken: string) => Promise<void>;
};

function isValidToken(tokenInput: string) {
  return tokenInput.startsWith("hf_");
}

function getValidationMessage(tokenInput: string) {
  if (tokenInput.length > 0 && !isValidToken(tokenInput)) {
    return "Invalid token. Tokens must begin with hf_";
  }

  return null;
}

export default memo(function APITokenInput(props: Props) {
  const { classes } = useStyles();
  // Token submitted to callback. Use this state for managing the 'clear token' flow
  const [submittedToken, setSubmittedToken] = useState<string>("");
  // Literal value in input
  const [tokenInput, setTokenInput] = useState<string>("");
  const [isAlertVisible, setIsAlertVisible] = useState<boolean>(true);

  const onSetToken = async () => {
    if (tokenInput.length > 0 && !isValidToken(tokenInput)) {
      return;
    }

    await props.onSetToken(tokenInput);
    // If clearing token, remind user to set it again
    setIsAlertVisible(tokenInput.length === 0);
    setSubmittedToken(tokenInput);
  };

  return (
    <Flex direction="column" style={{ padding: "0 1rem" }}>
      <Alert
        color="blue"
        hidden={!isAlertVisible}
        mb="8px"
        onClose={() => setIsAlertVisible(false)}
        title="Access Token"
        withCloseButton
      >
        For the best experience, it is recommended to set a temporary{" "}
        <Anchor
          href="https://huggingface.co/docs/hub/security-tokens#user-access-tokens"
          target="_blank"
          className={classes.tokenLink}
        >
          Hugging Face Access Token
        </Anchor>
        .
      </Alert>
      <Flex align="center" justify="flex-end" gap="sm">
        <TextInput
          placeholder="Paste your token here"
          type="password"
          value={tokenInput}
          onChange={(e) => setTokenInput(e.currentTarget.value)}
          error={getValidationMessage(tokenInput)}
        />
        <Button
          onClick={onSetToken}
          disabled={
            // Allow clearing token (set to empty after previously submitting a token)
            (tokenInput.length === 0 && submittedToken.length === 0) ||
            (tokenInput.length > 0 && !isValidToken(tokenInput))
          }
        >
          Set Token
        </Button>
      </Flex>
    </Flex>
  );
});
